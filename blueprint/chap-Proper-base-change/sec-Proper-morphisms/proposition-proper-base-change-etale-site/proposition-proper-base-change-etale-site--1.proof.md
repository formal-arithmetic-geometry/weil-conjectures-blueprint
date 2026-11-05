+++
kind = "proof"
of = "proposition-proper-base-change-etale-site--1"
order = 398002
uses = ["lemma-finite-morphisms", "lemma-composition-cancellation", "lemma-pbc-projective-space", "theorem-chow-s-lemma-projective-form"]
+++
The property is local on the target. Indeed, after an arbitrary base change
$Y'\to Y$, the inverse images of the affine opens of $Y$ cover $Y'$.
Restriction to these opens identifies the derived base change map with
the maps for the restrictions of $f$, and these restrictions detect
isomorphisms. We may therefore assume that $Y$ is affine.

The affine-base case of Theorem [theorem-chow-s-lemma-projective-form]
gives a proper surjection $\pi:\widetilde X\to X$ and a closed immersion
$i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y$ such that
$f\pi=q_Yi_Y$. No Noetherian or finite presentation hypothesis is needed.
Since $f$ is separated, the induced map

$$
i_X=(\pi,i_Y):\widetilde X\longrightarrow
X\times_Y\mathbf P^n_Y=\mathbf P^n_X
$$

is also a closed immersion, and $\pi=q_Xi_X$.

Closed immersions are finite, so $i_Y$ and $i_X$ satisfy
$\mathrm{PBC}_\Lambda$ by Lemma [lemma-finite-morphisms]. The projections
$q_Y$ and $q_X$ satisfy it by Lemma [lemma-pbc-projective-space].
Composition, in the torsion-coefficient case of
Lemma [lemma-composition-cancellation](i), gives the property for
$f\pi$ and $\pi$. Finally, $\pi$ is surjective, so part (ii) of that
lemma gives $\mathrm{PBC}_\Lambda(f)$.
