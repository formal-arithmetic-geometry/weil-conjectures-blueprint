+++
kind  = "proof"
of    = "det-cor-jacobian-torsion-kernel"
uses = ["sk-thm-av-final", "sk-prop-av-isogeny", "sk-prop-av-prime-p-etale", "sk-prop-av-finite-etale-points", "sk-thm-picard-main"]
+++
*(1)* By [sk-prop-av-isogeny] (part (a) of [sk-thm-av-final]), $[n]$ is a
finite flat surjective homomorphism of degree $n^{2g}$, so $A[n]$ is a
finite flat group scheme over $k$ of order $n^{2g}$. Since $n$ is
invertible in $k$, the order $n^{2g}$ is prime to $p=\operatorname{char}k$
(any order if $p=0$), so $A[n]$ is étale by [sk-prop-av-prime-p-etale].
Write $A[n]=\Spec B$ with $B$ a finite étale $k$-algebra of dimension
$n^{2g}$. A finite étale algebra over a field is a finite product of
finite separable field extensions; as $k$ is algebraically closed each
factor is $k$, so $B\simeq k^{n^{2g}}$ and
$A[n]\simeq\coprod_{r=1}^{n^{2g}}\Spec k$.

*(2)* By the universal property of the fibre product, for every $k$-scheme
$T$ the group $A[n](T)$ is the kernel of $[n]\colon A(T)\to A(T)$, which
is multiplication by $n$ in the group $A(T)$. For $T=\Spec k$ this gives
$A[n](k)=A(k)[n]$. A $k$-point of $\coprod_{r}\Spec k$ is the inclusion of
one of the $n^{2g}$ components, so $\lvert A[n](k)\rvert=n^{2g}$ (this is
the first half of [sk-prop-av-finite-etale-points]).

*(3)* Fibre products commute with base change, and the group law, the unit
and hence $[n]$ of $A_K$ are the base changes of those of $A$; therefore
$A[n]\times_kK=A_K[n]$. By (1),
$A[n]\times_kK\simeq\coprod_r\Spec K$, compatibly with the decomposition
over $k$: the $r$-th component $\Spec k$ base changes to the $r$-th
component $\Spec K$. The map $x\mapsto x_K$ sends the inclusion of the
$r$-th component over $k$ to the inclusion of the $r$-th component over
$K$, so it is a bijection between two sets of $n^{2g}$ elements (the
second half of [sk-prop-av-finite-etale-points]). It is a homomorphism
because base change $A(k)\to A_K(K)$ is a homomorphism of groups: it is
induced by the morphism of group functors $A(T)\to A(T\times_kK)$.

*(4)* By [sk-thm-picard-main] the formation of the Picard scheme and of
$J(C)=\operatorname{Pic}^0_{C/k}$ commutes with extension of the ground
field: $J(C)\times_kK$ represents the degree-zero part of the Picard
functor of $C_K/K$, and the resulting isomorphism
$J(C)\times_kK\xrightarrow{\sim}J(C_K)$ is the unique one compatible with
the representing data, hence an isomorphism of group schemes defined
without choices. An isomorphism of group schemes commutes with $[n]$, so
it restricts to an isomorphism $(J(C)\times_kK)[n]\simeq J(C_K)[n]$ and
induces a group isomorphism on $K$-points. Composing with the isomorphism
of (3) for $A=J(C)$ gives the claim. Both arrows are natural in $K$
(base change along $K\subset K'$ is compatible with the representing data),
so the composite is canonical.
