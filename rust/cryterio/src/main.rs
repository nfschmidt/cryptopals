extern crate clap;
use clap::{App, SubCommand};
use std::io::{self, Read};

extern crate encoding;

fn main() {
    let matches = App::new("cryterio")
                          .version("v0.1")
                          .author("Nicolas Schmidt <nfschmidt@gmail.com>")
                          .about("Cryptographic tools")
                          .subcommand(SubCommand::with_name("encode")
                                      .about("Encodes input with the specified encoding")
                                      .subcommand(SubCommand::with_name("hex")
                                                  .about("Encode input in hex"))
                                      .subcommand(SubCommand::with_name("base64")
                                                  .about("Encode input in base64")))
                          .get_matches();


    if let Some(matches) = matches.subcommand_matches("encode") {
        if let Some(_) = matches.subcommand_matches("base64") {
            run_encode_base64();
        } else if let Some(_) = matches.subcommand_matches("hex") {
            run_encode_hex();
        }
    } else {
        run_interpreter();
    }
}

fn run_encode_base64() {
}

fn run_encode_hex() {
    let result = encoding::hex_encode(io::stdin());
    print!("{}", result);
}

fn run_interpreter() {
    println!("Interpreter");
}
