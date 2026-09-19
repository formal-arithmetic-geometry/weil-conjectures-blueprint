+++
id = "chap-openclosed"
kind = "section"
title = "The open–closed exact sequence"
order = 968
+++
Let $X$ be a scheme, let $j\colon U\to X$ be an open immersion and let
$i\colon Z\to X$ be a closed immersion whose range is the complement of the
range of $j$. The goal of this chapter is the short exact sequence

$$
0\longrightarrow j_!j^*\mathcal F\longrightarrow\mathcal F
\longrightarrow i_*i^*\mathcal F\longrightarrow0
$$

of sheaves on the small étale site of $X$, for an arbitrary sheaf
$\mathcal F$ with values in a Grothendieck abelian category of coefficients.
It is the statement [thm-openclosed-exact] at the end of the chapter, and
everything before it is a step of its proof.

The sequence is classical — it is the excision sequence of étale
cohomology; see [MilneEtale] or [SGA4]. What this chapter
adds is a proof organised so that every step is a statement one can formalise,
and in particular a substitute for the dense-subsite argument that does not
work here ([rmk-openclosed-no-dense-subsite]).
