+++
kind = "proof"
of = "lemma-rigidification-along-section--2"
order = 1520006
uses = []
+++
The endomorphism $\psi^{-1}\circ\varphi$ of $\mathcal A$ is multiplication
by a global function $c$ on $Z$. By surjectivity, write $c=p^*b$ for a
global function $b$ on $B$. Pulling back along $s$ gives multiplication
by $b$, since $p\circ s=\mathrm{id}_B$. The equality
$s^*\varphi=s^*\psi$ says that this multiplication is the identity.
Multiplication by global functions on an invertible sheaf is faithful,
so $b=1$, and hence $\varphi=\psi$.

For the final assertion take $p=f_T$, $s=\sigma_T$, and
$\psi=\mathrm{id}$. Condition $(\ast)$ implies the required surjectivity
by `AlgebraicGeometry.surjective_appTop_of_isIso_pushforwardUnitMap`.
An automorphism preserving the chosen trivialization pulls back to the
identity along $\sigma_T$.
