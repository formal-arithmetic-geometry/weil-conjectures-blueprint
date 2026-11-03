+++
id = "prose-10-07"
kind = "hidden"
title = "Plan of the proof with finite coefficients"
order = 438
+++
With finite coefficients the six operations are already available on the
étale site, and we know $f^!$ on every chart. What is missing is a way
to compare charts, and the proof provides it in three steps of
increasing generality. On affine space the trace map, built from the
projective line, gives an explicit counit. On a vector bundle a change of
linear coordinates does not change this trace, because $\GL_d$ has
connected fibres, so the trace glues
(Proposition [sk-prop-an]). Finally, deformation to the normal
bundle reduces the general smooth morphism to its relative tangent
bundle along the diagonal (Proposition [sk-prop-sp-orientation]). The
first two steps are the content of the next subsection, and the third
occupies the two subsections after it.

With finite coefficients, smooth purity
(Proposition [sk-thm-smooth-purity]) says that for $f$ smooth
of pure relative dimension $d$, the exceptional inverse image $f^!$ is the
ordinary inverse image, twisted by $(d)$ and shifted by $[2d]$.

Fix $n\geq1$. We carry out the geometric calculation with
coefficients $\mathbf Z/\ell^n\mathbf Z$, and until Section [sec-sp-grp-ladic-summary] we
omit the subscript from functors, dualizing complexes and the maps
$\gamma_f$.
Thus $f^*$, $Rf_!$, $f^!$, $\omega_f$ and $\gamma_f$ refer to this
cyclic coefficient ring. Since the calculation extends
along $\mathbf Z/\ell^n\mathbf Z\to A$ when $\ell^nA=0$,
Proposition [sk-thm-smooth-purity] then gives the result
for every finite admissible ring $A$.

The functor $f^!$ and its local form for smooth $f$ were obtained in
Section [sec-finite-geometric] with $\Lambda=\mathbf Z/\ell^n\mathbf Z$,
and the adjunction for the projective line was proved in
Proposition [sk-prop-geo-p1-adjunction] and lifted to $\ell$-adic
coefficients in Proposition [sk-prop-diagonal-tower]. We recall the
explicit unit and counit below, because the passage to
towers in Section [sec-sp-grp-ladic-summary] repeats them level by level.
