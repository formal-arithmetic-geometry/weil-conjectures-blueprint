+++
id = "def-weil-unramified-morphism"
kind = "definition"
title = "Unramified morphism of schemes"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism", "def-pc-fibre-product", "def-weil-open-immersion"]
lean = ["AlgebraicGeometry.LocallyOfFiniteType", "AlgebraicGeometry.FormallyUnramified", "AlgebraicGeometry.FormallyUnramified.isOpenImmersion_diagonal"]
order = 16
tags = ["mathlib", "stacks-02GE"]
+++
A morphism of schemes $f:X\to Y$ [def-pc-scheme] is *unramified* if it is locally of finite type [def-weil-finite-type-morphism] and its diagonal $\Delta_f:X\to X\times_YX$ into the fibre product [def-pc-fibre-product] is an open immersion [def-weil-open-immersion]; equivalently, $f$ is locally of finite type and *formally unramified*, i.e. covered by affine opens $\operatorname{Spec}A\to\operatorname{Spec}R$ with $R\to A$ formally unramified. (By Stacks Lemma 02GE, parts (1) and (2), this is the notion of Stacks Definition 02G4, where $f$ is unramified if it is covered by affine opens $\operatorname{Spec}A\to\operatorname{Spec}R$ with $R\to A$ of finite type and $\Omega_{A/R}=0$.)
