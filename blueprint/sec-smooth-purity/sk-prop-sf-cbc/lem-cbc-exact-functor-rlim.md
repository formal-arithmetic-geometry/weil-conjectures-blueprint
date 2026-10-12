+++
id = "lem-cbc-exact-functor-rlim"
kind = "lemma"
title = "Exact functors commute with derived limits of towers"
order = 1890
uses = ["def-weil-pbc-derived-inverse-limit", "prop-weil-pbc-roos-triangle"]
+++
Let $F$ be a triangulated functor between the derived categories of
pro-etale module sheaves which is exact, commutes with the
levelwise evaluation of
[def-weil-pbc-derived-inverse-limit], and commutes with the
*countable* derived products of the tower category, i.e. the
canonical maps
$F(R\prod_nM_n)\to R\prod_nF(M_n)$ are isomorphisms for every
family $(M_n)_n$ (a triangulated functor preserves finite
products, hence only finite, not countable, products in general).
Then for every tower $M_\bullet\in D(\operatorname{Tow}(T))$ the
canonical map

$$
F\bigl(\Rlim M_\bullet\bigr)\xrightarrow{\ \sim\ }\Rlim F(M_\bullet)
$$

is an isomorphism.
