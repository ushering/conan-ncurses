#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class NcursesConan(ConanFile):
    name = "ncurses"
    version = "6.1"
    author = "Ruisheng Wang <ruisheng.wang@outlook.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. It uses terminfo format, supports pads and color and multiple highlights and forms characters and function-key mapping, and has all the other SVr4-curses enhancements over BSD curses. SVr4 curses became the basis of X/Open Curses."
    homepage = "https://www.gnu.org/software/ncurses"
    settings = "os", "compiler", "build_type", "arch"
    source_subfolder = "source_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        source_url = "https://invisible-mirror.net/archives/ncurses/ncurses-{}.tar.gz".format(self.version)
        tools.get(source_url)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        with tools.chdir(self.source_subfolder):
            configure_args = ['--without-debug',
                              '--without-normal',
                              '--enable-widec',
                              '--without-ada',
                              '--disable-db-install',
                              '--without-manpages',
                              '--without-progs',
                              '--without-tack',
                              '--without-tests',
                              '--without-cxx-binding',
                              '--without-cxx']
            env_build.configure(args=configure_args)
            env_build.make()
            env_build.install()

    def package_info(self):
        self.cpp_info.libs = ['panelw','ncursesw'] # note that the order matters since 'ncursesw' depends on 'panelw'
