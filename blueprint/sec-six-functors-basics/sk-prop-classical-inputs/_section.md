+++
id = "sk-prop-classical-inputs"
kind = "proposition"
title = "Results from the étale theory"
order = 2601
uses = ["sk-def-cd"]
tags = ["sketch"]
+++
- *Proper base change*: let $p:X\to S$ be proper, let $g:S'\to S$ be a
  morphism, and let $p':X'\to S'$, $g':X'\to X$ be the projections of
  $X'=X\times_SS'$. For $K\in D_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$,
  the base change map $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism. In
  particular, the geometric stalk of $Rp_*K$ is the pro-étale cohomology of the
  fibre.
- *Finiteness*: for $f$ separated of finite type, $Rf_!$ maps
  $\Dbc(X,\Lambda)$ into $\Dbc(S,\Lambda)$.
- *Cohomological dimension*: the direct images
  $Rf_*,Rf_!:D^+_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)\to
  D^+_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$ along morphisms of schemes
  of finite type over $k$ have finite cohomological amplitude on classical
  pro-étale coefficient sheaves, and hence $\operatorname{cd}_\ell(f)<\infty$ in
  the sense of [sk-def-cd].
