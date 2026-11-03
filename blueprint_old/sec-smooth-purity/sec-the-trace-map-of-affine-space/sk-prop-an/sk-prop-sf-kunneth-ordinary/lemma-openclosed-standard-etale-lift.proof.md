+++
kind  = "proof"
of    = "lemma-openclosed-standard-etale-lift"
+++
No witness of the standard-étale condition is lifted; lifting one naively
does not work, since a lift of the identity witnessing the condition only
holds modulo $I$. Instead the pair over $R$ is chosen so that the condition
holds for free, using two observations.

*For a monic $f$ and an arbitrary $g$, the pair $(f,g\cdot f')$ is
standard étale.* Indeed $f'$ divides $(g f')^1$, so the condition
$g^n\in(f',f)$ holds with $n=1$ and the witness $(g,0)$.

*Replacing $g$ by $g\cdot f'$ does not change the algebra:*

$$
S[T][1/(g f')]/(f)\cong S[T][1/g]/(f),
$$

because $f'$ is already invertible in $S[T][1/g]/(f)$ — that is exactly the
standard-étale condition for $(f,g)$ — so inverting it again changes
nothing. Formally, the image of $T$ on either side satisfies the universal
property of the other standard étale algebra, and the two induced maps are
mutually inverse.

Now lift $\bar f$ to a monic $F\in R[T]$ of the same degree, lift $\bar g$ to
an *arbitrary* $G\in R[T]$, and put $H:=G\cdot F'$. By the first
observation $(F,H)$ is a standard étale pair over $R$, and the algebra of a
standard étale pair base changes to the algebra of the pair with reduced
coefficients. The reduction of $(F,H)$ along $R\to R/I$ is
$(\bar f,\bar g\cdot\bar f')$, whose algebra is $(R/I)[T][1/\bar g]/(\bar f)$
by the second observation. That is the asserted isomorphism.
