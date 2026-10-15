+++
kind = "proof"
of = "sk-prop-ctf-finite-compact"
uses = ["sk-lem-sf-flat-model", "sk-lem-formal-closed-support", "sk-cor-pe-finite-tor-comparison", "sk-prop-pe-unbounded-classical"]
+++
We first prove, on the étale site, compactness against arbitrary objects of $\D(X_{\mathrm{ét}},A)$. By
[sk-lem-sf-flat-model] it suffices to treat $a_!L$. Factor $a=i\circ u$ with $i\colon Z\hookrightarrow X$ closed
and $u\colon S\hookrightarrow Z$ open, and let $j\colon X\setminus Z\hookrightarrow X$ be the complementary open
immersion. Since $L$ has finite projective stalks, it is dualizable with dual
$L^\vee=\underline{\operatorname{Hom}}_A(L,A_S)$, and the étale form of part (2) of
[sk-lem-formal-closed-support] gives, for $K\in\D(X_{\mathrm{ét}},A)$,

$$
R\operatorname{Hom}_X(a_!L,K)=R\Gamma\bigl(S,L^\vee\otimes_Au^*R\underline\Gamma_ZK\bigr),
\qquad R\underline\Gamma_ZK=i^*\fib\bigl(K\to Rj_*j^*K\bigr).
$$

Every functor on the right, as a functor between étale derived categories, preserves arbitrary direct
sums. For $Rj_*$ and $R\Gamma(S,-)$ this is Stacks, Tag 0F11: a derived direct image of finite cohomological
dimension commutes with direct sums of unbounded complexes. It applies to $A$-modules because derived
direct image and global sections commute with forgetting the coefficient ring (Stacks, Tag 0D6J). The
other functors are inverse images, tensor products with finite projective sheaves, and a fiber. Taking
$H^0$ gives compactness of $a_!L$. Shifts, finite extensions and direct summands preserve compactness, so
[sk-lem-sf-flat-model] extends it to all of $\Dctf(X_{\mathrm{ét}},A)$ ([det-ctf-finite-compact-etale]).

To pass to the pro-étale site, use [sk-cor-pe-finite-tor-comparison] and [sk-prop-pe-unbounded-classical]:
the inverse image $\nu_X^*\colon\D(X_{\mathrm{ét}},A)\to\D(X_{\mathrm{proét}},A)$ is exact, fully faithful and
coproduct-preserving, so it identifies the localizing closures of the corresponding finite-Tor
constructible objects. Compactness against all étale complexes therefore gives compactness in
$\Loc(\Dctf(X,A))$ ([det-ctf-finite-compact-proetale]). The identification of this localizing closure with
the whole étale derived category is [sk-prop-ctf-finite-comparison].

Constructibility and finite Tor amplitude are preserved by direct summands, so $\Dctf(X,A)$ is thick. It is
essentially small, being a full subcategory of the essentially small bounded constructible category. A
skeleton generates $\Loc(\Dctf(X,A))$ by definition, and the usual compact-generation argument (Stacks,
Tag 09SN and the finite factorization argument in Stacks, Tag 09SM) identifies the compact objects with the
thick closure of this skeleton, which is $\Dctf(X,A)$ ([det-ctf-finite-compact-generators]).
