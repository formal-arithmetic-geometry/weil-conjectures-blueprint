+++
kind  = "proof"
of    = "lemma-weil-pbc-stein-connectedness"
+++
*Step 1 (finiteness).* The finiteness of $A\to B$ is not proved in this
blueprint; it is input (i) of [thm-weil-pbc-stein-inputs], where the
Noetherian reference and the approximation route available here are recorded.
We use it as a hypothesis for the rest of the proof.

*Step 2 (the pair $(B,IB)$ is henselian).* This is proved here. Given a
finite $B$-algebra $C$, the composite $A\to C$ is finite: finiteness is
closed under composition in the sense of
[def-weil-pbc-scheme-conventions]. For such a $C$, every idempotent of $C/IC$
lifts uniquely to an idempotent of $C$, because $(A,I)$ is henselian
[def-weil-pbc-henselian-terminology] and a finite $A$-algebra is in
particular integral over $A$. That is precisely the definition of the pair
$(B,IB)$ being henselian.

*Step 3 (connectedness).* This is not proved in this blueprint; it is input
(ii) of [thm-weil-pbc-stein-inputs], the henselian-pair proper-base-change
theorem stating that for $Z$ proper over $\operatorname{Spec}A$ every
irreducible closed subset of $Z$ meets $Z\times_AA/I$ in a nonempty connected
subset. Applied to $Z=Y$ it gives the connectedness clause of the statement.

*Step 4 (spectrality and closedness).* This is proved here. $Y$ is spectral
[def-weil-pbc-scheme-conventions]: $p$ is separated and of finite type, so
$Y$ is quasi-compact and quasi-separated, and the underlying space of a
scheme is sober with a basis of quasi-compact opens. The subscheme
$Y_0\subset Y$ is closed, since
$S_0=\operatorname{Spec}(A/I)\to\operatorname{Spec}A$ is a closed immersion
and closed immersions are stable under base change by
[lem-weil-pbc-closed-immersion-products].

*Step 5.* Steps 3 and 4 verify the hypotheses of the Zariski restriction
criterion [lemma-weil-pbc-spectral-restriction] for the pair $(Y,Y_0)$, so its
conclusion applies to $(Y,Y_0)$; the last assertion of the statement follows.
We repeat the warning of input (iii) of [thm-weil-pbc-stein-inputs]: that
criterion is available for *locally constant* sheaves only, and the
constructible sheaf to which the degree-zero argument applies it is not known
to be locally constant.

Fix an irreducible closed subset and give it the reduced closed-subscheme
structure $C\subseteq X$. The map $C\to S$ is proper. Its Stein
factorization gives $C\xrightarrow{u}\operatorname{Spec}B \xrightarrow{v}S$, with $A\to B$ integral and $u$ having geometrically
connected fibres. Since $(A,\mathfrak m)$ is henselian,
$(B,\mathfrak mB)$ is a henselian pair. The image
$D=v(\operatorname{Spec}B)$ is irreducible and closed because $C\to S$ is
proper. Henselian connectedness makes $D\cap V(\mathfrak m)$ connected and
nonempty. The map
$C\cap X_0\to D\cap V(\mathfrak m)$ is closed and surjective with connected
fibres, so the closed-surjection connected-fibre criterion makes
$C\cap X_0$ connected. This expands Tag
`0A0B`; the final equality of sections is Lemma
[lemma-weil-pbc-spectral-restriction].
