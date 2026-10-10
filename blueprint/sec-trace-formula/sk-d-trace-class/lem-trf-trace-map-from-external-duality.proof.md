+++
kind  = "proof"
of    = "lem-trf-trace-map-from-external-duality"
+++
Let $\Delta:X\to X\times_sX$ be the diagonal. The external product
of [def-trf-external-product] pulls back to
$K\otimes_A^LD_XK$. The definition of the Verdier dual in
[def-trf-dualizing-complex], evaluation for internal Hom, and the
symmetry of the derived tensor in [def-weil-derived-tensor] give
$K\otimes_A^LD_XK\to\omega_{X,A}$.
By the pullback/direct-image adjunction of
[def-weil-derived-pullback-tensor-hom], its adjoint is

$$
e_K:K\boxtimes_A^LD_XK\longrightarrow R\Delta_*\omega_{X,A}.
$$

Assuming the comparison requested in [thm-trf-verdier-duality],
apply $Rc^!$ to this map and form

$$
\begin{aligned}
\mathcal H_c(K)&\xrightarrow{\sim}Rc^!(K\boxtimes_A^LD_XK)\\
&\xrightarrow{Rc^!e_K}Rc^!R\Delta_*\omega_{X,A}\\
&\xrightarrow{\sim}Ri_{F*}Rd^!\omega_{X,A}\\
&\xrightarrow{\sim}Ri_{F*}\omega_{F,A}.
\end{aligned}
$$

The last two arrows are the exceptional form of fixed-square base
change in [thm-trf-fixed-point-base-change] and the composition
of dualizing complexes in [thm-trf-dualizing-complex-composition].
Taking derived global sections gives $\mathfrak t_{c,K}$.
Equivalently, adjunction along $i_F$ gives
$\theta_{c,K}:Li_F^*\mathcal H_c(K)\to\omega_{F,A}$.
Thus this objectwise map is a consequence of the external duality
[thm-trf-verdier-duality], which is proved; the construction is
unconditional.
