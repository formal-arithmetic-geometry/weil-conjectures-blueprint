+++
kind = "proof"
of = "lemma-rigidification-along-section--3"
order = 1520007
uses = ["lemma-rigidification-along-section--1"]
+++
Suppose that $\mathcal L$ and $\mathcal L'$ have the same image under the
displayed map. Equality of their images in $\operatorname{Pic}_{C/S}(T)$
gives an invertible sheaf $\mathcal N$ on $T$ and an isomorphism

$$
\mathcal L\simeq\mathcal L'\otimes f_T^*\mathcal N
$$

by `AlgebraicGeometry.exists_iso_tensorObj_of_toPicardFunctor_app_eq`.
This follows by choosing an fppf cover on which the two classes agree
and descending their ratio from the base using $(\ast)$.
Pulling back along $\sigma_T$ and using
$\sigma_T^*\mathcal L\simeq\sigma_T^*\mathcal L'$ gives
$\mathcal N\simeq\mathcal O_T$ by cancellation of an invertible sheaf.
Thus $[\mathcal L]=[\mathcal L']$, proving injectivity.

For surjectivity, let $([\mathcal N],x)$ belong to the product. By
[lemma-rigidification-along-section--1], choose a normalized class
$[\mathcal L_0]$ mapping to $x$. Then
$\mathcal L_0\otimes f_T^*\mathcal N$ pulls back to $\mathcal N$ along
$\sigma_T$ and still maps to $x$. The latter assertion is
`AlgebraicGeometry.toPicardFunctor_app_eq_of_iso`: a sheaf from the base
is Zariski-locally trivial, so twisting by it does not change the image
in the relative Picard sheaf.

Finally, $\sigma_T^*f_T^*\mathcal N\simeq\mathcal N$ follows from
$f_T\circ\sigma_T=\mathrm{id}_T$, as in
`AlgebraicGeometry.pullbackSectionBaseChangeSndIso`. This proves the
retraction identity and injectivity of $f_T^*$; the two statements about
twists from the base give exactness in the middle, and the bijection
gives surjectivity on the right.
