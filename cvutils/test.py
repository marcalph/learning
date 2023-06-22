

from pathlib import Path
import pandas as pd
import json
import cv2

# compile annotations
### >> jq -n '[ inputs | .json_id = input_filename ]'  flash_contour_thresh_200/*.json > compiled_annotations
# read annotations 
class Annotations():
    def __init__(self, path: Path) -> None:
        self.path = path
    
    def read_labels(self) -> None:
        with open(self.path) as fh:
            data = json.load(fh)
        self.df = pd.json_normalize(data, 'detected_flashes', ['json_id'])
        self.df['area'] = self.df['bbox.w'] * self.df['bbox.h']
        self.df['video_id'] = self.df.json_id.apply(lambda x: self._get_video_id(x))
    # read video frame and dump them
    def _extract_bbox(self, video_path: str, frame_number: int, x:int, y:int, w:int, h:int) -> None:
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        for fn in range(max(1,frame_number-20), min(total_frames, frame_number+20)):
            cap.set(1, fn)
            ret, frame = cap.read()
            if ret:
                ymax, xmax = frame.shape[:2]
                bbox = frame[max(0,y-5):min(ymax,y+h+5), max(0, x-5):min(xmax, x+w+5)]
                cv2.imwrite(f"data/flashdet/flashdet_anno/{Path(video_path).name}-{fn}.png", bbox)

    # upload dataset
    def upload_to_spine(self):
        pass

    @staticmethod
    def _get_video_id(json_id: str):
        json_path = Path(json_id)
        return f"{json_path.name.split('_flashes')[0]}.mp4"
    
    @staticmethod
    def _get_videos_from_flashdet_anno():
        images_from_anno = Path('data/flashdet/flashdet_anno').rglob("*.png")
        videos_from_anno = [x.name.split(".mp4")[0]+".mp4" for x in images_from_anno]
        return videos_from_anno

        
    
    

if __name__ == "__main__":
    pwd = Path("/Users/marcalph/hs/flashdet/compiled_annotations.json")
    ano = Annotations(pwd)
    ano.read_labels()
    print(ano.df)
    print(ano.df.describe())
    print(ano.df.video_id.unique())
    ## derive from annotations
    # ano.df.apply(
    #     lambda row: ano._extract_bbox(f"/Users/marcalph/hs/flashdet/trimmed_videos/{row.video_id}",
    #                                   row.frame_index,
    #                                   row['bbox.x'],
    #                                   row['bbox.y'],
    #                                   row['bbox.w'],
    #                                   row['bbox.h']), axis=1) # type: ignore
    ## some manual filtering was done
    videoset = set([x.name for x in (pwd.parent/"trimmed_videos").rglob("*.mp4")])
    missingset = videoset - set(ano._get_videos_from_flashdet_anno())
    print(missingset)
    print([x for x in missingset if "TRUE" in x])
    flashdet_anno = Path('data/flashdet/flashdet_anno/').rglob("*.png")
    res = ["T" if "TRUE" in x.name else  "F" for x in flashdet_anno]
    from collections import Counter
    print(Counter(res))

