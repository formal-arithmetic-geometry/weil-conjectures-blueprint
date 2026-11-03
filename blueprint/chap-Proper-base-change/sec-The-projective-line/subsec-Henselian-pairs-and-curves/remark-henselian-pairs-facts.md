+++
id = "remark-henselian-pairs-facts"
kind = "remark"
title = "Facts on henselian pairs"
name_showing = false
order = 354
+++
- (i) *Gabber's affine analogue of proper base change.*
  If $(B,J)$ is a henselian pair and $G$ is a torsion abelian sheaf on
  $\operatorname{Spec}(B)_{\acute{e}t}$, restriction induces
  $$
  H^q(\operatorname{Spec}B,G)
  \xrightarrow{\sim}
  H^q(\operatorname{Spec}(B/J),G|)
  \qquad(q\geq0).
  $$
  This is [Stacks, [09ZI](https://stacks.math.columbia.edu/tag/09ZI)], and its proof is an effacement argument on affines.
- (ii) *Lifting finite étale covers over a proper henselian pair.*
  If $Y$ is proper over a henselian pair $(B,J)$, and
  $Y_0=Y\times_B B/J$, then restriction is an equivalence between the categories of finite
  étale schemes over $Y$ and over $Y_0$,
  $$
  \textit{F\'Et}_Y\xrightarrow{\sim}
  \textit{F\'Et}_{Y_0}.
  $$
  This is [Stacks, [0GS2](https://stacks.math.columbia.edu/tag/0GS2)], proved by algebraization, approximation, and
  descent of finite presentation.  In particular, for a finite abelian
  group $M$, we obtain
  $$
  H^1(Y,\underline M)\xrightarrow{\sim}H^1(Y_0,\underline M).
  \tag{4.8}
  $$
  Indeed, these groups classify $M$-torsors, and the equivalence transports
  finite étale covers, their group actions, and the equations expressing
  simple transitivity.
