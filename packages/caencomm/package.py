# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Caencomm(Package):
    """CAEN Communications library"""

    homepage = "https://www.caen.it/products/caencomm-library/"
    url = "https://scisoft.fnal.gov/scisoft/reference_tarballs/CAENComm-v1.6.0.tgz"

    version("1.6.0", sha256="d6fea92074c78a8c030664a0086dd26820d25ab200444db5cd4f088bb5760334")

    depends_on("caenvmelib")

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        install_tree("include", prefix.include)

        if self.spec.target.family == "aarch64":
            install_tree("lib/arm64", prefix.lib)
        elif self.spec.target.family == "x86":
            install_tree("lib/x86", prefix.lib)
        else:
            install_tree("lib/x64", prefix.lib)

        libs = find(prefix.lib, "libCAENComm*")
        print(libs)
        for lib in libs:
            symlink(lib, prefix.lib + "/libCAENComm.so")

        mkdirp(prefix + "/doc")
        install("*.txt", prefix + "/doc")
