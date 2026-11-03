+++
kind  = "proof"
of    = "lem-weil-geometric-generic-duality"
+++
On an affine open of $X$, choose a closed immersion
$i:X\hookrightarrow\mathbf A^r_{\mathbf A^1_k}$ over
$\mathbf A^1_k$. Composition of the ambient adjunctions of
[thm-amb-etale-exceptional-adjoint] and the explicit affine-space
adjunction [cor-amb-affine-space-adjunction] compute

$$
\omega_X=Ri^!A(r+1)[2r+2],\qquad
\omega_{X_{\bar\eta}}=Ri_{\bar\eta}^!A(r)[2r].
$$

Apply closed-support generic exchange from
[lem-weil-geometric-generic-exchange]; an invertible constant
twist and shift commute with this right adjoint by tensor adjunction.
This gives the first comparison. It is compatible with the
evaluations defining duality, since it was obtained from composition
and the adjunction counits.

Both $K$ and $D_XK$ are bounded constructible of finite Tor
amplitude by [lem-weil-verdier-preservation-strata].
The internal-Hom comparison in
[lem-weil-geometric-generic-exchange] can therefore be applied
twice. Writing $L=A(1)[2]$, the first application gives
$g^*D_XK=D_{X_{\bar\eta}}(g^*K)\otimes L$; the second gives

$$
g^*D_XD_XK
=D_{X_{\bar\eta}}D_{X_{\bar\eta}}(g^*K),
$$

because $D(Q\otimes L)=D(Q)\otimes L^{-1}$.
Evaluation compatibility and [lem-weil-duality-pairing]
identify the pulled-back double-dual arrow with the one on the
generic fibre. The construction is needed only locally for checking
the arrow on geometric stalks; its compatibility with open restriction
is [lem-weil-delta-restriction].
