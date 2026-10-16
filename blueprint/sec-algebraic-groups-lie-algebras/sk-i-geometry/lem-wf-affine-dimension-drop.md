+++
id = "lem-wf-affine-dimension-drop"
kind = "lemma"
title = "Proper closed subsets have strictly smaller dimension"
lean = ["ringKrullDim_quotient_lt_of_irreducibleSpace", "PrimeSpectrum.isDomain_of_irreducibleSpace"]
order = 2829
+++
Let $X$ be an irreducible affine variety over a field $k$, with
coordinate algebra $k[X]$ (finitely generated and reduced). Then $k[X]$
is a domain, and every closed subset $Y\subsetneq X$ satisfies
$\dim Y\le\dim X-1$ (with the convention $\dim\varnothing=-1$), where
dimension is the supremum of lengths of strict chains of prime ideals of
the coordinate algebra.
