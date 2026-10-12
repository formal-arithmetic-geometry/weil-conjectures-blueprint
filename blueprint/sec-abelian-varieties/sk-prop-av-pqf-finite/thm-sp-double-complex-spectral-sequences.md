+++
id = "thm-sp-double-complex-spectral-sequences"
kind = "theorem"
title = "The two spectral sequences of a first-quadrant double complex"
order = 524
uses = ["def-sp-convergence", "def-sp-double-complex-total", "def-sp-image-filtration", "thm-sp-spectral-object-yields"]
+++
Let $D^{\bullet,\bullet}$ be a first-quadrant double complex in an abelian
category, with total complex $\operatorname{Tot}(D)$ and first and second
filtrations ${}'F$, ${}''F$ as in [def-sp-double-complex-total]. Each
filtration determines, through its bigraded exact couple and the derived
couples, a first-quadrant spectral sequence:

- (I) the *first spectral sequence* ${}'E$, of the filtration ${}'F$, with
  $$
   {}'E_1^{p,q}=H^q_{II}(D^{p,\bullet}),\qquad
   {}'E_2^{p,q}=H^p_IH^q_{II}(D),
  $$
  $d_1$ being induced by $d_I$;
- (II) the *second spectral sequence* ${}''E$, of the filtration ${}''F$,
  indexed by the filtration degree $q$ first, with
  $$
   {}''E_1^{q,p}=H^p_{I}(D^{\bullet,q}),\qquad
   {}''E_2^{q,p}=H^q_{II}H^p_I(D),
  $$
  $d_1$ being induced by $d_{II}$.

Both abut to $H^\bullet(\operatorname{Tot}D)$: for $F$ either of the two
filtrations, the image filtration [def-sp-image-filtration]

$$
 F^pH^n=\operatorname{im}\bigl(H^n(F^p\operatorname{Tot}D)
 \longrightarrow H^n(\operatorname{Tot}D)\bigr)
$$

satisfies $F^0H^n=H^n(\operatorname{Tot}D)$ and $F^{n+1}H^n=0$, so it is
finite in each degree, and $E_\infty^{p,q}\cong
\operatorname{gr}^pH^{p+q}(\operatorname{Tot}D)$ in the sense of
[def-sp-convergence]; moreover each entry stabilizes, $E_r^{p,q}=
E_\infty^{p,q}$ for $r>\max(p,q+1)$. Convergence is thus automatic. Both
spectral sequences are functorial for morphisms of double complexes.
