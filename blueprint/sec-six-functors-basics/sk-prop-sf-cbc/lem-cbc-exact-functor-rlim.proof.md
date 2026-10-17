+++
kind  = "proof"
of    = "lem-cbc-exact-functor-rlim"
+++
By [def-weil-derived-limit], $R\varprojlim_nM_n$ is the first term of the Roos
triangle

$$
R\varprojlim_nM_n\to\prod_nM_n\xrightarrow{1-s}\prod_nM_n
\to\bigl(R\varprojlim_nM_n\bigr)[1].
$$

The functor $F$ is triangulated, so applying $F$ produces a distinguished
triangle with first term $F(R\varprojlim_nM_n)$. Under the isomorphisms
$F(\prod_nM_n)\cong\prod_nF(M_n)$ the image of $1-s$ is the transition
endomorphism $1-F(s)$ of the system $(F(M_n),F(f_n))_n$, since both are
determined by their components $M_m\to M_n$. Hence $F(R\varprojlim_nM_n)$ is
the first term of a Roos triangle for $(F(M_n))_n$, that is, a derived limit
of this system in the sense of [def-weil-derived-limit]. Any two such objects
are isomorphic, by an isomorphism compatible with the maps to
$\prod_nF(M_n)$ (non-uniquely in general, as for cones).
