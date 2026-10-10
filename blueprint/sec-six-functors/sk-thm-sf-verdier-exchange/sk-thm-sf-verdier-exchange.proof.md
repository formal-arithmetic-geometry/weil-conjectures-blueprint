+++
kind  = "proof"
of    = "sk-thm-sf-verdier-exchange"
+++
*Step 1:* $Rf^!\omega_Y\cong\omega_X$: by the composition law and
[sk-lem-sf-mate], the mate of $R(a_Y\circ f)_!\cong Ra_{Y!}Rf_!$ is the
isomorphism $Rf^!Ra_Y^!\cong Ra_X^!$. *Step 2:* apply
[sk-thm-sf-tensor-hom] with $N=\omega_Y$ and substitute Step 1:
$\mathbb D_Y(Rf_!M)=\RHom_Y(Rf_!M,\omega_Y)\cong Rf_*\RHom_X(M,f^!\omega_Y)\cong Rf_*\RHom_X(M,\omega_X)=Rf_*\mathbb D_XM$.
Naturality and the compatibilities are those of the two ingredients. (This
proof uses only the tensor–Hom exchange and never the duality chapter, which
is what removes the proof cycle between the framework and duality chapters.)
