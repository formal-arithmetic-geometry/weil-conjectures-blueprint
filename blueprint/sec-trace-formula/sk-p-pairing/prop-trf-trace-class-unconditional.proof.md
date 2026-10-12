+++
kind  = "proof"
of    = "prop-trf-trace-class-unconditional"
+++
By [def-trf-trace-class] the trace class is the composite

$$
A\xrightarrow{\ \widetilde u\ }
R\Gamma(C,\mathcal H_c(K))\xrightarrow{\ \mathfrak t_{c,K}\ }
R\Gamma(F,\omega_{F,A})
$$

followed by the identification of the target with
$\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$, where
$A=A_{E,n}$ is the coefficient ring of
[def-trf-coefficient-conventions].
The first arrow is the mate of $u$ under the tensor–internal-Hom
adjunction of [def-trf-trace-class-source], which is defined for
every correspondence $u$ and needs no hypothesis. The second arrow
is the morphism $\mathfrak t_{c,K}$ of
[lem-trf-trace-map-from-external-duality]: its construction
applies the external duality
[thm-trf-verdier-duality] — itself a consequence of the
Kunneth–Verdier chain [thm-trf-kunneth-verdier] — to the
external product of the dualizing data of
[def-trf-dualizing-complex], and its inverse comparisons are the
ones supplied by the supported pairing of
[def-trf-supported-pairing]. Both arrows therefore exist as soon
as the correspondence $c$ is admissible in the sense of
[def-trf-correspondence] and the fixed scheme is the one of
[def-trf-fixed-scheme], which is the assertion.
