#!/bin/bash
function write_echoer_file {
    cat > $1 << 'END'
#!/bin/bash
echo $1
END
    chmod +x $1
}
write_echoer_file echoer
./echoer 'Hello world'