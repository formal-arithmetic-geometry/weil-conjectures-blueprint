+++
id = "def-weil-weakly-etale-morphism"
kind = "definition"
title = "Weakly etale morphism of schemes"
uses = ["def-weil-flat-morphism", "def-pc-fibre-product"]
refines = "def-weil-scheme-morphism-properties"
lean = ["AlgebraicGeometry.WeaklyEtale"]
tags = ["sheaf-dag", "mathlib", "stacks-094P"]
+++
A morphism of schemes $f:X\to Y$ is *weakly étale* (or *absolutely flat*) if $f$ is flat [def-weil-flat-morphism] and its diagonal morphism $\Delta_f:X\to X\times_YX$ into the fibre product [def-pc-fibre-product] is flat.
