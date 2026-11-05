+++
kind = "proof"
of = "lemma-reciprocal-roots-zeta--5"
order = 1389011
+++
Write $A(T)=\prod_a(1-aT)$ and $B(T)=\prod_b(1-bT)$ over
$\overline{\mathbf Q}$. The reciprocal roots $a$ and $b$ are roots of the
monic integral polynomials $U^{\deg A}A(U^{-1})$ and $U^{\deg B}B(U^{-1})$.
Hence they are nonzero algebraic integers. Let
$\theta:\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_\ell$ be an embedding, and
let $a$ be a reciprocal root of $A$ or $B$. By
(19.2) and the pairwise coprimality of the
$P_{i,\ell}$, there is exactly one $i$ such that $\theta(a)$ is a
Frobenius eigenvalue on $H^i_\ell$. It is odd for $A$ and even for $B$.

Corollary [corollary-purity-cohomology-smooth-proper-variety] bounds
$|\iota(\theta(a))|$ for embeddings $\iota$ of $\overline{\mathbf Q}_\ell$. The lemma,
however, concerns the embeddings of the number field $\mathbf Q(a)$. We
pass from one to the other by extending field embeddings. Let
$\tau:\mathbf Q(a)\hookrightarrow\mathbf C$ be any embedding. The map
$\tau\circ\theta^{-1}$, defined on $\theta(\mathbf Q(a))$, extends to a
field isomorphism $\iota':\overline{\mathbf Q}_\ell\xrightarrow{\sim}\mathbf C$, because both
are algebraically closed fields of characteristic zero with
transcendence degree $2^{\aleph_0}$ over $\mathbf Q$. We have
$\iota'(\theta(a))=\tau(a)$. Applying
Corollary [corollary-purity-cohomology-smooth-proper-variety] with this $\iota'$ to the
eigenvalue $\theta(a)$ on $H^i_\ell$, we find

$$
|\tau(a)|=q^{i/2}.
$$

Since $q>1$, this absolute value determines $i$, and so $i$ does not
depend on $\theta$.

*Source:* the proof of Lemma [lemma-reciprocal-roots-zeta].
