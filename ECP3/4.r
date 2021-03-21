#!/usr/bin/Rscript
library(bnlearn)

dag <- empty.graph(nodes = c("Máquina","E","M","Nova","Usada"))
arc.set <- matrix(c("Máquina", "E",
                    "Máquina", "M",
                    "E", "Nova",
                    "E", "Usada",
                    "M", "Nova",
                    "M", "Usada"),
                  byrow = TRUE, ncol = 2,
                  dimnames = list(NULL, c("from", "to")))
arcs(dag) <- arc.set
nodes(dag)

arcs(dag)

plot(dag)