#faas build -f functemp.yml --shrinkwrap
varDirectory=temperatura
sudo buildctl build \
    --frontend dockerfile.v0 \
    --local context=build/$varDirectory \
    --local dockerfile=build/$varDirectory/ \
    --output type=image,name=docker.io/evaristo00/$varDirectory"15":latest,push=true
    
#faas deploy -f prueba.yml
