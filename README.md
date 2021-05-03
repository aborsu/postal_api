# Postal API

This is an API Wrapper around [libpostal](https://github.com/openvenues/libpostal).
Current version is provided via the conda-forge feedstock for [libpostal](https://github.com/conda-forge/libpostal-feedstock) and [postal](https://github.com/conda-forge/postal-feedstock).

If you want to know what it does: 

Some reasons behind the choice of making this into an API:
 * Libpostal takes ~800MB of space 
 * libpostal and postal are not compatible with windows

This api is not rate throttled and requires no authentication... don't make me do it.
