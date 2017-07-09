alias rustc='docker run --rm -it -v $(pwd):/app -v $(pwd)/.cargo/.registry:/home/app/.cargo/registry rustdev rustc '
alias cargo='docker run --rm -it -v $(pwd):/app -v $(pwd)/.cargo/.registry:/home/app/.cargo/registry rustdev cargo '
