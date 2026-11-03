+++
kind  = "proof"
of    = "det-lem-formal-closed-support-derived"
uses = ["det-lem-formal-closed-support-sheaves", "sk-prop-sf-open-closed-triangle"]
+++
K-injective resolutions with injective terms exist in
$\Mod(X_{\mathrm{proét}},\Lambda)$, a Grothendieck abelian category ([Stacks, Tag 079P](https://stacks.math.columbia.edu/tag/079P)).

*(1)* Represent $K$ by a K-injective complex $I^\bullet$. Then
$R\underline\Gamma_ZK=\underline\Gamma_ZI^\bullet$, which is K-injective by
[det-lem-formal-closed-support-sheaves] (3). Since $i_*$ is exact it needs no
deriving, and for a complex $A$ on $Z$
$$
\Hom_{\D(X)}(i_*A,K)=\Hom_{K(X)}(i_*A,I^\bullet)=\Hom_{K(Z)}(A,\underline\Gamma_ZI^\bullet)=\Hom_{\D(Z)}(A,R\underline\Gamma_ZK),
$$
the middle equality being the termwise adjunction of
[det-lem-formal-closed-support-sheaves] (2). The same identity holds for the
Hom complexes (which compute $R\operatorname{Hom}$ because $I^\bullet$ and
$\underline\Gamma_ZI^\bullet$ are K-injective), giving the $R\operatorname{Hom}$
form.

*(2)* The map $j_!j^*I\to j_*j^*I$ (adjoint to the identity of $j^*I$, using
$j^*j_!=\mathrm{id}$) is a monomorphism: it is the identity after $j^*$, and
$i^*j_!=0$, so its kernel $\kappa$ satisfies $j^*\kappa=0$ and
$i^*\kappa\subset i^*j_!j^*I=0$, whence $\kappa=0$ by the localization
sequence. By injectivity of $I$, the inclusion $j_!j^*I\hookrightarrow I$ (the
counit) extends to $s\colon j_*j^*I\to I$. Let $\eta\colon I\to j_*j^*I$ be the
unit and $e=\eta\circ s$. Then $j^*e=\mathrm{id}$, since after $j^*$ all of
$j_!j^*I\to I\to j_*j^*I$ and $j_!j^*I\to j_*j^*I$ become the identity of
$j^*I$. As $j_*$ is fully faithful, $e=j_*j^*e=\mathrm{id}$. So $\eta$ has a
section and is surjective.

*(3)* Represent $K$ by a K-injective complex $I^\bullet$ with injective terms.
The functor $j^*$ has the exact left adjoint $j_!$, so $j^*I^\bullet$ is
K-injective and $Rj_*j^*K=j_*j^*I^\bullet$. By
[det-lem-formal-closed-support-sheaves] (1) and (2) above, the sequences
$$
0\to i_*\underline\Gamma_Z(I^n)\to I^n\to j_*j^*I^n\to0
$$
are exact for every $n$ and form a short exact sequence of complexes. A short
exact sequence of complexes gives a distinguished triangle in the derived
category; its first term is $i_*\underline\Gamma_ZI^\bullet=i_*R\underline\Gamma_ZK$,
and its second arrow represents the unit $K\to Rj_*j^*K$. Morphisms of $K$
lift to morphisms of K-injective resolutions, unique up to homotopy, so the
triangle is natural. Hence $i_*R\underline\Gamma_ZK\simeq\fib(K\to Rj_*j^*K)$;
applying the exact functor $i^*$ and $i^*i_*=\mathrm{id}$
([sk-prop-sf-open-closed-triangle]) gives the fiber formula.
