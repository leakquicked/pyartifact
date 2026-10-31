# PyArtifact

Create a local inventory of file names, sizes and SHA-256 digests.

## Requirements
Python 3.10+, standard library only.

## Usage
`python pyartifact.py --help`

Processes local files only; no network requests or uploads. Do not publish confidential inventories.

## Tests
`python -m unittest discover -s tests -v`
