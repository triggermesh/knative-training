all: build open

build: 
	marp --pdf --allow-local-files knative.md
open:
	open knative.pdf
