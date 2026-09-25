+++
id = "lem-trf-trace-map-etale-pullback"
kind = "lemma"
title = "Pullback of the trace map"
order = 2474
uses = ["lem-trf-trace-map-from-external-duality", "lem-trf-trace-source-etale-pullback", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-verdier-duality"]
+++
With the identifications of
[lem-trf-trace-source-etale-pullback], the trace morphisms of
[lem-trf-trace-map-from-external-duality] for $c,K$ and for
$c',K'$ satisfy

$$
Le_F^*\mathfrak t_{c,K}
\;=\;
\mathfrak t_{c',K'},
$$

after applying $R\Gamma(C,\cdot)$ and the projection formula, i.e.
the square

$$
\begin{array}{ccc}
Le_C^*R\Gamma(C,\mathcal H_c(K))&\xrightarrow{\ Le_C^*\mathfrak t_{c,K}\ }&
Le_F^*R\Gamma(F,\omega_{F,A})\\
\Big\downarrow{\scriptstyle \sim}&&\Big\downarrow{\scriptstyle \sim}\\
R\Gamma(C',\mathcal H_{c'}(K'))&\xrightarrow{\ \mathfrak t_{c',K'}\ }&
R\Gamma(F',\omega_{F',A})
\end{array}
$$

commutes, the vertical isomorphisms being the pullback and
dualizing-data comparisons.

## Proof

By [lem-trf-trace-map-from-external-duality] the trace morphism is
the composite

$$
R\Gamma(C,\mathcal H_c(K))\to R\Gamma(C,Rc^!(K\boxtimes_A^LD_XK))
\to R\Gamma(F,\omega_{F,A}),
$$

whose four constituent maps are (i) the Kunneth–Verdier isomorphism
[thm-trf-verdier-duality], (ii) the pullback of the evaluation
pairing, (iii) the exceptional fixed-square base change
[thm-trf-fixed-point-base-change], and (iv) the dualizing
composition [thm-trf-dualizing-complex-composition]. Each of the
four is compatible with the etale base change along $e$: for (i) this
is the functoriality of the external duality in the correspondence and
in $K$, which is exactly the content of
[lem-trf-trace-source-etale-pullback]; for (ii) the evaluation
pairing is natural, and the pullback of $K\boxtimes_A^LD_XK$ is
$K'\boxtimes_A^LD_{X'}K'$ by monoidality of the pullback and the
pullback of the dualizing complex; for (iii) the fixed square of $c'$
is the base change of the fixed square of $c$, and the exceptional
base change is compatible with further base change; for (iv) the
dualizing composition is functorial in the morphism. Composing the
four compatibilities gives the commutativity of the displayed square,
which is the assertion.
