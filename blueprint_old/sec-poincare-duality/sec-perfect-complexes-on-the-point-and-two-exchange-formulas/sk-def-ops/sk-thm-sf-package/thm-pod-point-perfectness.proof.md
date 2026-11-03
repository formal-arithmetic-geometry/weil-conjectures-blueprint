+++
kind  = "proof"
of    = "thm-pod-point-perfectness"
+++
*Step 1: the finite level.* Let $\Lambda=A=A_{E,n}$ and let
$K\in D^b_{ctf}(X,A)$ have Tor amplitude in $[a,b]$
([def-weil-finite-torsion-constructibility],
[def-weil-finite-tor-amplitude]). At the geometric point $s$ a bounded
constructible complex is a bounded complex of $A$-modules with finite
cohomology ([def-weil-finite-coefficient-point]), and the Tor
amplitude of a complex on $s$ is the Tor amplitude of the underlying
$A$-module complex, since the sheaves of $A$-modules on $s$ are the
$A$-modules.

For ordinary cohomology, apply [cor-sf-direct-image-ctf-proetale]
to the separated finite-type morphism $a_X:X\to s$: the complex
$Ra_{X,*}K$ is bounded constructible with Tor amplitude in
$[a,b+2d]$. Hence $R\Gamma(X,K)$ is bounded, has finite cohomology
modules, and has Tor amplitude in $[a,b+2d]$. No properness is used.

For compact support, choose a compactification $a_X=\bar a\circ j$
with $j:X\hookrightarrow\bar X$ an open immersion and $\bar a$ proper
([def-compact-support-direct-image-detailed]); replacing $\bar X$ by
the scheme-theoretic closure of $X$ we may assume $\dim\bar X\leq d$.
Then $Ra_{X,!}K=R\bar a_*j_!K$. Extension by zero is exact and
commutes with derived tensor product, as one checks on stalks, so
$j_!K$ is bounded constructible with Tor amplitude in $[a,b]$, and
[cor-sf-direct-image-ctf-proetale] applied to $\bar a$ gives Tor
amplitude in $[a,b+2d]$ for $R\Gamma_c(X,K)$. The finiteness and
boundedness of its cohomology is
[prop-trf-compact-support-perfectness].

By [lem-trf-finite-tor-amplitude-perfect], a bounded complex of
$A$-modules with finite cohomology and Tor amplitude in $[a',b']$ is
quasi-isomorphic to a complex $P^\bullet$ of finite free $A$-modules
with $P^i=0$ for $i\notin[a',b']$. Hence $R\Gamma(X,K)$ and
$R\Gamma_c(X,K)$ are represented by bounded complexes of finite free
$A$-modules in degrees $[a,b+2d]$. For such a $P^\bullet$ the derived
dual $P^{\bullet\vee}=R\operatorname{Hom}_A(P^\bullet,A)$ is computed
termwise, $P^\bullet$ being a bounded complex of projectives, and is
the complex of finite free modules $\operatorname{Hom}_A(P^{-i},A)$
in degrees $[-b-2d,-a]$. Thus all four complexes are perfect point
complexes in the sense of [def-pod-perfect-point-complex], with the
stated amplitudes.

*Step 2: integral coefficients.* Put $R=\mathcal O_E$, $A_n=A_{E,n}$, and
let $K\in\Dctf(X,R)=\Dbc(X,R)$, a full subcategory of
$D(X_{\mathrm{pro\acute et}},R)$, with reductions
$K_n=K\otimes^L_{\mathcal O_{E,X}}A_n$. By [sk-prop-integral-criterion] each
$K_n$ lies in $\Dbc(X,A_n)$, and by [lem-coef-integral-residue-tor] all the
$K_n$ have Tor amplitude in one interval $[a,b]$, namely the cohomological
range of $K_1$. By Step 1 every $R\Gamma(X,K_n)$ and $R\Gamma_c(X,K_n)$ is a
bounded complex of finite free $A_n$-modules in the common interval
$[a',b']=[a,b+2d]$.

By [sk-lem-finite], $R\Gamma(X,K)=Ra_{X*}K$ and $R\Gamma_c(X,K)=Ra_{X!}K$ are
perfect complexes over $R$: they lie in $\Dctf(s,R)$, whose objects have
bounded finitely generated cohomology, and $R$ is a discrete valuation ring,
of global dimension one. In particular they lie in
$D^b_{\mathrm{fg}}(R)$. By [sk-prop-scalar-six], reduction modulo $\pi_E^n$
commutes with $Ra_{X*}$ and $Ra_{X!}$:

$$
R\Gamma(X,K)\otimes^L_RA_n\simeq R\Gamma(X,K_n),\qquad
R\Gamma_c(X,K)\otimes^L_RA_n\simeq R\Gamma_c(X,K_n).
$$

The common amplitude follows. Let $C$ be one of these two complexes; then
$C\otimes^L_RA_1$ has cohomology in $[a',b']$. Over the discrete valuation
ring $R$, $C\simeq\bigoplus_iH^i(C)[-i]$, and $C\otimes^L_RA_1$ has
$H^i(C)/\pi_EH^i(C)$ in degree $i$ and the $\pi_E$-torsion $H^i(C)[\pi_E]$ in
degree $i-1$. The $H^i(C)$ are finitely generated, so by Nakayama
$H^i(C)=0$ for $i\notin[a',b']$, and $H^{a'}(C)$ is torsion-free, hence
free. Each $H^i(C)$ with $i>a'$ has a two-term free resolution in degrees
$[i-1,i]$. Hence $C$ is represented by a bounded complex of finite free
$R$-modules in degrees $[a',b']$, and its reductions are perfect with
amplitude in $[a',b']$, independent of $n$.

For the duals, if $P^\bullet$ is a bounded complex of finite free
$R$-modules representing $C$, then $C^\vee$ is the termwise dual
complex, again bounded and finite free, and
$C^\vee\otimes^L_RA_n\cong\operatorname{Hom}_{A_n}(P^\bullet\otimes_RA_n,A_n)=C_n^\vee$;
by Step 1 these reductions are perfect in the common interval
$[-b',-a']$.

*Step 3: the field coefficients.* For $\Lambda=E$, [sk-lem-finite] shows
directly that the four complexes are perfect over the field $E$, that is,
bounded with finite-dimensional cohomology. The same follows from Step 2 by
integral models: $K$ is obtained by finitely many cones and shifts from
objects $(a_!L_0)[1/\ell]$ with integral $L_0$ ([sk-lem-integral-models]),
and by [sk-prop-scalar-six] $R\Gamma$ and $R\Gamma_c$ commute with
$-\otimes_RE$, which is exact. For $\Lambda=\Qlb$, $K$ is the extension of
scalars of some $K'\in\Dbc(X,E')$ with $E'/\Ql$ finite
([sk-thm-sfb-qlbar-two-colimit]); the four complexes are obtained from the
$E'$-complexes by the exact extension of scalars $-\otimes_{E'}\Qlb$
([sk-prop-scalar-six]), which preserves boundedness and
finite-dimensionality and commutes with the dual of a complex with
finite-dimensional total cohomology. This proves the field assertions.

*Step 4: the proper case.* If $X_0$ is proper, then $a_X$ is proper
and the comparison $R\Gamma_c(X,K)\to R\Gamma(X,K)$ of
[def-weil-ordinary-compact-cohomology] is an isomorphism at each
coefficient ring, compatible with the constructions above.
