+++
kind = "proof"
of = "corollary-unramified-boundary-point--2"
order = 1183003
uses = ["lemma-boundary-stalk", "proposition-weights-j-boundary-points", "proposition-weights-under-usual-operations"]
+++
By Lemma [lemma-boundary-stalk], the adjunction map identifies
$\mathcal G$ with $j_*j^*\mathcal G$. Proposition
[proposition-weights-j-boundary-points], applied to the lisse sheaf
$j^*\mathcal G$, therefore gives weights $\le a$ for $\mathcal G$.
This is the step
`AlgebraicGeometry.WeilSheaf.IsLisse.hasWeightsAtMost_of_upperStar`.

The dual $\mathcal G^\vee$ is lisse. At a closed point of $U_0$, the
stalk of $j^*\mathcal G^\vee$ identifies with the dual of the stalk of
$\mathcal G$ at its image in $X_0$. Purity of $j^*\mathcal G$ and the
dual rule in Proposition [proposition-weights-under-usual-operations]
thus give purity of weight $-a$ for $j^*\mathcal G^\vee$. Applying the
same upper-bound step to $\mathcal G^\vee$ gives weights $\le -a$
on all of $X_0$.

For every closed point $x$, the Frobenius-equivariant identification
$(\mathcal G^\vee)_{\bar x}\simeq(\mathcal G_{\bar x})^\vee$ is supplied by
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalk_dual`.
If $\alpha$ is a Frobenius eigenvalue on $\mathcal G_{\bar x}$, the two
bounds give
$$
|\iota(\alpha)|\le q_x^{a/2},\qquad
|\iota(\alpha^{-1})|\le q_x^{-a/2}.
$$
Since Frobenius is invertible, $\alpha\ne0$, and these inequalities force
$|\iota(\alpha)|=q_x^{a/2}$. This last step is
`FrobeniusModule.IsPureOfWeight.of_hasWeightsAtMost_of_equiv_dual`.
