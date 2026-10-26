+++
id = "lem-cbc-exact-functor-rlim"
kind = "lemma"
title = "Exact functors commute with derived limits of towers"
order = 2683
uses = ["def-weil-derived-limit"]
+++
Let $F:\mathcal D\to\mathcal D'$ be a triangulated functor between
triangulated categories with countable products (for instance derived
categories of module sheaves on a pro-étale site), and assume that $F$
commutes with countable products, i.e. the canonical maps
$F(\prod_nM_n)\to\prod_nF(M_n)$ are isomorphisms for every family $(M_n)_n$
(a triangulated functor preserves finite products, but not countable ones in
general). Then for every inverse system $(M_n,f_n)_n$ in $\mathcal D$ with
derived limit $R\varprojlim_nM_n$ in the sense of [def-weil-derived-limit],
$F(R\varprojlim_nM_n)$ is a derived limit of $(F(M_n),F(f_n))_n$:

$$
F\bigl(R\varprojlim_nM_n\bigr)\xrightarrow{\ \sim\ }R\varprojlim_nF(M_n).
$$
