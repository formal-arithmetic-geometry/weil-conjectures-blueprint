+++
kind  = "proof"
of    = "lem-pc-universal-divisor"
+++
By the definition of representability ([def-pc-hilb-functor]) the
universal element is a closed subscheme
$D_{\mathrm{univ}}\subset X_H=H\times_SX$ which is finite locally free of
degree $d$ over $H$. The projection $H\times_SX\to H$ is the base change of
$X\to S$, hence smooth of relative dimension $1$. Applying
[lem-pc-cartier-criterion] ((1)$\Rightarrow$(2)) to it and to
$D_{\mathrm{univ}}$ shows that $D_{\mathrm{univ}}$ is a relative effective
Cartier divisor on $H\times_SX$ over $H$
([def-pc-relative-effective-cartier]). Its associated invertible module is
$\mathcal{O}(D_{\mathrm{univ}})$ ([def-pc-divisor-line-bundle]).

Let $h:T\to H$ be a morphism of $S$-schemes. By universality, the closed
subscheme $D_h\subset X_T$ classified by $h$ is the pullback of
$D_{\mathrm{univ}}$ along $h\times\mathrm{id}_X:X_T\to H\times_SX$, i.e. its base
change along $h$. Since $H\times_SX\to H$ is flat and locally of finite
presentation (being smooth), [lem-pc-recd-pullback] gives
$\mathcal{O}_{X_T}(D_h)\cong(h\times\mathrm{id}_X)^*\mathcal{O}(D_{\mathrm{univ}})$.

For the last assertion take $S=\operatorname{Spec}(k)$, $X$ as in
[thm-pc-hilb-curves] and $h=[D]:\operatorname{Spec}(k)\to H$ a $k$-rational
point. By [thm-pc-hilb-curves](2) it corresponds to the element $D$ of
$\operatorname{Hilb}^{d}_{X/k}(k)$, so $D_h=D\subset X$, and the restriction of
$\mathcal{O}(D_{\mathrm{univ}})$ to $[D]\times X\cong X$ is $\mathcal{O}_X(D)$.
