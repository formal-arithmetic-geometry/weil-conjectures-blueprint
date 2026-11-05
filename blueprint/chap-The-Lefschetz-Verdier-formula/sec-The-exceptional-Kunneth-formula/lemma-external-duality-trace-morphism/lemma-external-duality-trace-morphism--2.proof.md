+++
kind = "proof"
of = "lemma-external-duality-trace-morphism--2"
order = 910002
uses = ["lemma-external-duality-trace-morphism--1", "proposition-six-operations-dctf", "proposition-composition-open-restriction-compactifications-f", "proposition-construction-independence-rf-shriek", "proposition-projection-formula-rational-coefficients"]
+++
The composition isomorphisms for $c_2=p_2c$ and $c_1=p_1c$ identify
$\mathcal H_c(K)$ with
$\cHom_{\Qbarl}(c^*p_2^*K,c^!p_1^!K)$. This is
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClassSourceIso`.

For $P,Q\in\Dbc(X\times_kX,\Qbarl)$, the exceptional Hom exchange is

$$
\cHom_{\Qbarl}(c^*P,c^!Q)\xrightarrow{\sim}
c^!\cHom_{\Qbarl}(P,Q).
$$

Indeed, for every $T\in\Dbc(C,\Qbarl)$, tensor–Hom adjunction,
$Rc_!\dashv c^!$ and the projection formula give

$$
\begin{aligned}
\Hom(T,\cHom_{\Qbarl}(c^*P,c^!Q))
&\simeq\Hom(c^*P\otimes^{\mathbf L}T,c^!Q)\\
&\simeq\Hom(Rc_!(c^*P\otimes^{\mathbf L}T),Q)\\
&\simeq\Hom(P\otimes^{\mathbf L}Rc_!T,Q)\\
&\simeq\Hom(T,c^!\cHom_{\Qbarl}(P,Q)).
\end{aligned}
$$

The projection formula for $Rc_!$ is obtained from its compactification
and the proper projection formula
[proposition-projection-formula-rational-coefficients]. Yoneda gives
the exchange isomorphism, as in
`CategoryTheory.Verdier.isIso_exceptionalHomMap_of_isIso` and
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.exceptionalHomIso`.
Apply it with $P=p_2^*K$ and $Q=p_1^!K$, then compose with $c^!$ of the
inverse of $\kappa_{K,K}$ from [lemma-external-duality-trace-morphism--1].
