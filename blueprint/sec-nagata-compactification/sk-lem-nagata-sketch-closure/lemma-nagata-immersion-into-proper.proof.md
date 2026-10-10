+++
kind  = "proof"
of    = "lemma-nagata-immersion-into-proper"
+++
Write $f\colon X\to S$ for the composite. Since $Y\to S$ is proper, it is
separated, hence quasi-separated; as $f$ is quasi-compact,
[lemma-nagata-open-immersion-qc-over-separated-target] applied to the
triangle $X\xrightarrow{g}Y\to S$ shows that $g$ is quasi-compact. Thus $g$
is a quasi-compact immersion and $\mathsf C(g)$ is defined
([def-nagata-immersion-compactification]). Its first map $g^{\mathrm{im}}$
is a (quasi-compact) open immersion by
[lemma-nagata-immersion-open-in-scheme-image]. The second map is the
composite of the closed immersion $g_{\mathrm{im}}$ with the proper map
$Y\to S$, hence is proper. The factorization equality gives the required
structural equality:

$$
g^{\mathrm{im}};g_{\mathrm{im}};(Y\to S)
=g;(Y\to S)=f.
$$

So $\mathsf C(g)$ is a compactification of $f$ in the sense of
[def-nagata-compactification], and $f$ is compactifiable
([def-nagata-compactifiable]).
