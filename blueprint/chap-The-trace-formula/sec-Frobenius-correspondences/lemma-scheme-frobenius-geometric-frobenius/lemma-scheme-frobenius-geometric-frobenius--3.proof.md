+++
kind = "proof"
of = "lemma-scheme-frobenius-geometric-frobenius--3"
order = 953006
uses = ["lemma-comparison-via-relative-frobenius", "definition-frobenius-operator", "lemma-scheme-frobenius-geometric-frobenius--2", "lemma-scheme-frobenius-geometric-frobenius--4"]
+++
Apply the Frobenius comparison for the lower shriek to the structure morphism
$a_X:X\to\operatorname{Spec}k$, with the identity endomorphism on the base.
The comparison square has $p=\operatorname{id}_X$, $f'=a_X$, and
$r=\Phi_m$, which is a finite universal homeomorphism by assumption.
Expanding the Weil structure on compactly supported cohomology gives

$$
F^W_{c,m}(K,\phi)=\RGammac(X,\phi_m)\circ\Phi_m^\sharp.
$$

In Lean, `AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius_eq`
identifies the comparison with the unit defining compact pullback;
`AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_eq`
applies this to the iterated Weil object and removes the identifications
of its underlying complex with $K$.

The graph formula [lemma-scheme-frobenius-geometric-frobenius--4] gives the
first equality. If $\Phi$ is proper, use
[lemma-scheme-frobenius-geometric-frobenius--2] to replace the underlying
morphism of $\phi_m$ by $\psi_m$ in the displayed composite. This is the
definition of $F_{c,m}(\psi)$.
