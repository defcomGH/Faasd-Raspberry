#faas build -f functemp.yml --shrinkwrap
varDirectory=humedadlocal
sudo buildctl build \
    --frontend dockerfile.v0 \
    --local context=build/$varDirectory \
    --local dockerfile=build/$varDirectory/ \
    --output type=image,name=docker.io/evaristo00/humedadlocal20:latest,push=true
    
#faas deploy -f prueba.yml
