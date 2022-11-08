#faas build -f functemp.yml --shrinkwrap
varDirectory=temperatura15
sudo buildctl build \
    --frontend dockerfile.v0 \
    --local context=build/$varDirectory \
    --local dockerfile=build/$varDirectory/ \
    --output type=image,name=docker.io/evaristo00/$varDirectory:latest,push=true
    
#faas deploy -f prueba.yml
