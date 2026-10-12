+++
id = "def-weil-etale-morphism"
kind = "definition"
title = "Etale morphism of schemes"
uses = ["def-pc-scheme", "def-sbc-locally-finite-presentation", "def-weil-flat-morphism", "def-weil-unramified-morphism"]
lean = ["AlgebraicGeometry.Etale"]
tags = ["sheaf-dag", "mathlib", "stacks-02GI"]
+++
A morphism of schemes $f:X\to Y$ [def-pc-scheme] is *étale* if it is locally of finite presentation [def-sbc-locally-finite-presentation], flat [def-weil-flat-morphism] and unramified [def-weil-unramified-morphism]. (This is the notion of Stacks Definition 02GI, where $f$ is étale if it is covered by affine opens $\operatorname{Spec}A\to\operatorname{Spec}R$ with $R\to A$ an étale ring map: by Stacks Lemma 02GV $f$ is étale exactly when it is flat and G-unramified, and by Lemma 02GE a morphism locally of finite presentation is G-unramified exactly when its diagonal is an open immersion.)
