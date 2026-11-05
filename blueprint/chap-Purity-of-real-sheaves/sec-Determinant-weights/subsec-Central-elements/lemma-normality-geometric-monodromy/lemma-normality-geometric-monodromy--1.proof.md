+++
kind = "proof"
of = "lemma-normality-geometric-monodromy--1"
order = 1130001
uses = ["definition-monodromy-groups"]
+++
For any subgroup $\Gamma\subseteq\GL(k^n)$, its vanishing ideal
$I(\Gamma)$ is radical: if $f^m$ vanishes on $\Gamma$ for some $m>0$,
then $f$ vanishes there since $k$ is a field.

The identity belongs to $\Gamma$, so the counit vanishes on
$I(\Gamma)$. Inversion preserves $\Gamma$, so the antipode preserves
$I(\Gamma)$. For multiplication, put
$A=k[\GL(k^n)]/I(\Gamma)$. The image of the comultiplication of
$f\in I(\Gamma)$ in $A\otimes_k A$ evaluates at
$(\gamma,\delta)\in\Gamma\times\Gamma$ to $f(\gamma\delta)=0$.
The evaluations on $\Gamma$ separate elements of $A$, and their pairwise
tensor products separate elements of $A\otimes_k A$. Hence this image
is zero, proving that $I(\Gamma)$ is a Hopf ideal.
This is the argument of
`Matrix.GeneralLinearGroup.instIsHopfIdealVanishingIdeal`, using
`Algebra.TensorProduct.eq_zero_of_forall_liftQuotient_eq_zero`.

Apply this to $\rho(P)$ and $\rho(W)$. Since
$\rho(P)\subseteq\rho(W)$, every equation vanishing on $\rho(W)$
vanishes on $\rho(P)$, giving $I_G\subseteq I_H$ and $H\subseteq G$.
