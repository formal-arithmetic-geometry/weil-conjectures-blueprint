+++
kind  = "proof"
of    = "lem-sc-finite-extension-affine-model"
+++
By [lem-fin-normalization-extension-finite] the integral
closure $B'$ of the affine coordinate ring $B$ in $L$
is finite over $B$. It is a normal domain. Every element
of $L$ becomes integral over $B$ after multiplication by a
nonzero element of $B$, by clearing the coefficients of its
algebraic equation; hence $\operatorname{Frac}(B')=L$.
The construction of [def-fin-normalization-extension]
gives $C'=\operatorname{Spec}B'$. Integral extensions preserve
dimension, so $C'$ has dimension one. Its local rings at
closed points are regular by [lem-sc-normal-dim1-dvr];
at the generic point its local ring is a field.
A regular scheme of finite type over the perfect field $k$
is smooth. This last local algebra criterion is
[Stacks Project,
Tag 00TV](https://stacks.math.columbia.edu/tag/00TV), applied to its essentially finite-type local rings.
This proves the assertion.
