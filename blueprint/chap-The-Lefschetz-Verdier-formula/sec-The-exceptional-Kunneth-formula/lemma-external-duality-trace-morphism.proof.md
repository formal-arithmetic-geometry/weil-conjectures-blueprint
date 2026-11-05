+++
kind = "proof"
of = "lemma-external-duality-trace-morphism"
order = 911
uses = ["proposition-w-local-components", "definition-tate-twists", "lemma-flat-models-generators", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-finite-coefficients", "lemma-base-change-along-product-projection", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "theorem-sp-qbar", "proposition-compatibility-purity-base-change", "definition-trace-map", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "proposition-exceptional-external-kunneth"]
+++
The exceptional Künneth formula
(Proposition [proposition-exceptional-external-kunneth]) and the ordinary one
give Künneth formulas for internal Hom and for Verdier
duals, and these give the two displayed isomorphisms.

*Internal Hom and Verdier duals.*
On the point this is the identity
$\Hom(V_1,W_1)\otimes\Hom(V_2,W_2)=\Hom(V_1\otimes V_2,W_1\otimes W_2)$
for finite free modules.
For $E_i,L_i\in D^b_{\mathrm{ctf}}(X_i,A)$ the external comparison
$\cHom_A(E_1,L_1)\boxtimes\cHom_A(E_2,L_2)\to
\cHom_A(E_1\boxtimes E_2,L_1\boxtimes L_2)$ is an isomorphism. By
dévissage it suffices to check this on generators $E_i=Rh_{i!}F_i$, with $h_i$ the
inclusion of a stratum and $F_i$ a lisse sheaf with finite projective stalks
(Lemma [lemma-flat-models-generators]), for
which

$$
\cHom_A(Rh_{i!}F_i,L_i)
\simeq Rh_{i*}(F_i^\vee\otimes^{\mathbf L} h_i^!L_i).
$$

By the ordinary Künneth formula and $\alpha$, the exterior product of
these expressions is identified with internal Hom on the product. Taking
$L_i=\omega_{X_i}$ and using $\alpha$ for the structure maps, we get,
for $M_i\in D^b_{\mathrm{ctf}}(X_i,A)$,

$$
\mathbb D_{X_1\times X_2}(M_1\boxtimes M_2)
\simeq \mathbb D_{X_1}M_1\boxtimes \mathbb D_{X_2}M_2.
$$

*The two isomorphisms.*
The first isomorphism is the sheaf version of
$\Hom(V,W)\simeq W\otimes V^\vee$, and we obtain it by writing
internal Hom as a dual of a tensor product. Indeed, for $M\in D^b_{\mathrm{ctf}}(U,A)$, $N\in D^b_{\mathrm{ctf}}(V,A)$ and the projections
$p_U,p_V$ of $V\times U$, Verdier exchange and biduality let us rewrite
$\cHom_A(p_U^*M,p_V^!N)$ as
$\mathbb D_{V\times U}(\mathbb D_VN\boxtimes M)$. By the formula for
duals of exterior products this is
$N\boxtimes \mathbb D_UM$. Taking $M=N=K$, with the
factors of the product ordered as above, we obtain the first isomorphism.
The second isomorphism follows from the canonical exchange of exceptional inverse
image with Hom, for $P,Q\in D^b_{\mathrm{ctf}}(X\times X,A)$,

$$
c^!\cHom_A(P,Q)\simeq\cHom_A(c^*P,c^!Q),
$$

applied to $P=p_2^*K$ and $Q=p_1^!K$. To prove the exchange, we
use Yoneda inside $\Loc(D^b_{\mathrm{ctf}}(C,A))$, the category on which
$c_!\dashv c^!$ is defined
(Theorem [theorem-exceptional-inverse-image]). Test objects in all
of $D(C_{\mathrm{pro}\acute{e}t},A)$ would not do, since $c^!$ is not defined there. Both
sides of the exchange lie in $D^b_{\mathrm{ctf}}(C,A)$ by
Proposition [proposition-six-operations-dctf], so these test objects
suffice. By Proposition [proposition-comparison-etale-derived-category]
the localizing categories are $D(C_{\acute{e}t},A)$ and $D((X\times X)_{\acute{e}t},A)$,
where the projection formula for $c_!$ holds for all objects
[Stacks, [0GL5](https://stacks.math.columbia.edu/tag/0GL5)], and tensoring with $c^*P$ preserves $\Loc(D^b_{\mathrm{ctf}}(C,A))$.
For $M$ in $\Loc(D^b_{\mathrm{ctf}}(C,A))$ we obtain

$$
\begin{aligned}
\Hom\bigl(M,c^!\cHom_A(P,Q)\bigr)
&\simeq\Hom\bigl(c_!M\otimes^{\mathbf L}P,Q\bigr)
\simeq\Hom\bigl(c_!(M\otimes^{\mathbf L}c^*P),Q\bigr)\\
&\simeq\Hom\bigl(M\otimes^{\mathbf L}c^*P,c^!Q\bigr)
\simeq\Hom\bigl(M,\cHom_A(c^*P,c^!Q)\bigr),
\end{aligned}
$$

by $c_!\dashv c^!$ and the tensor–Hom adjunction, the projection formula,
$c_!\dashv c^!$ again, and the tensor–Hom adjunction.
