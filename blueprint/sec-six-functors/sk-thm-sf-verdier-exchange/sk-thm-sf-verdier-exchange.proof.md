+++
kind = "proof"
of = "sk-thm-sf-verdier-exchange"
uses = ["sk-thm-sf-tensor-hom", "sk-thm-pd-verdier-duality", "sk-lem-sf-mate", "sk-thm-sf-comp-composition"]
+++
Two formulas are [sk-thm-sf-tensor-hom]. Apply them to
the Verdier dual of the argument and use biduality ([sk-thm-pd-verdier-duality]) on both
schemes to obtain the other two. Compatibility follows from that of evaluation and the
adjunction comparisons.

*Complement.* By the composition law [sk-thm-sf-comp-composition] and [sk-lem-sf-mate], the
mate of $R(a_Y\circ f)_!\cong Ra_{Y!}Rf_!$ is the isomorphism $Rf^!Ra_Y^!\cong Ra_X^!$, that
is, $Rf^!\omega_Y\cong\omega_X$. Apply [sk-thm-sf-tensor-hom] with $N=\omega_Y$ and substitute
this isomorphism:

$$
\mathbb D_Y(Rf_!M)=\cHom_Y(Rf_!M,\omega_Y)\cong Rf_*\cHom_X(M,Rf^!\omega_Y)
\cong Rf_*\cHom_X(M,\omega_X)=Rf_*\mathbb D_XM.
$$

Naturality and the compatibilities are those of the two ingredients.
