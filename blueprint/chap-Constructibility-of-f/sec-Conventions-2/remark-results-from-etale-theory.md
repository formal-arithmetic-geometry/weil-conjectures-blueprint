+++
id = "remark-results-from-etale-theory"
kind = "remark"
title = "Results from the étale theory"
order = 532
uses = ["theorem-proper-base-change-classical-pro"]
+++
- *Proper base change*: let $p:X\to S$ be proper, let $g:S'\to S$ be
  a morphism, and let $p':X'\to S'$, $g':X'\to X$ be the projections of
  $X'=X\times_SS'$. For $K\in D_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the
  base change map $g^*Rp_*K\to Rp'_*g'^*K$ is
  an isomorphism. On the étale site this is
  Theorem [theorem-proper-base-change-classical-pro] for bounded below torsion complexes
  and [Stacks, [0F0C](https://stacks.math.columbia.edu/tag/0F0C)] for unbounded complexes with finite coefficients, and
  by comparison it holds on the pro-étale site. In particular, the
  geometric stalk of $Rp_*K$ is the pro-étale cohomology of the fibre.
- *Finiteness*: for $f$ separated of finite type,
  [Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)] says, after comparison with the étale site, that $Rf_!$ maps
  $\Dbc(X,\Lambda)$ into $\Dbc(S,\Lambda)$.
- *Cohomological dimension*: by [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)], the étale
  direct images along morphisms of schemes of finite type over $k$ have
  finite cohomological amplitude on torsion sheaves. By comparison, the
  same bound holds for
  $Rf_*,Rf_!:D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)\to
  D^+_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ on classical pro-étale
  coefficient sheaves, and hence $\operatorname{cd}_\ell(f)<\infty$ in the
  sense of Definition [definition-cohomological-dimension].
