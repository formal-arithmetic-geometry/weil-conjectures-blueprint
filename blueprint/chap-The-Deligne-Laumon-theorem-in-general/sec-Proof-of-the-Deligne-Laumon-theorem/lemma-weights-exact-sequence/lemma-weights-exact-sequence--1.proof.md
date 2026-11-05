+++
kind = "proof"
of = "lemma-weights-exact-sequence--1"
order = 1349002
uses = ["proposition-weights-under-usual-operations--1", "proposition-weights-under-usual-operations--2", "proposition-weights-under-usual-operations--3", "proposition-weights-under-usual-operations--5"]
+++
Put $K=\ker(b)$ and let $i:K\to F$ be its inclusion. Exactness makes
the induced map $F'\to K$ an epimorphism. Quotient stability therefore
gives $K$ a mixed filtration of weights at most $u$.

Put $Q=\operatorname{coker}(i)$, the coimage of $b$. The induced map
$Q\to F''$ is a monomorphism, so subobject stability gives $Q$ the
same upper weight bound. These are the bounded forms of
[proposition-weights-under-usual-operations--3]: take images of a
mixed filtration for a quotient, and intersect it with a subobject.
The resulting graded pieces are subquotients of the original pure
pieces, and retain their weights by
[proposition-weights-under-usual-operations--1] and
[proposition-weights-under-usual-operations--2].

Finally, apply extension stability
[proposition-weights-under-usual-operations--5] to

$$
0\to K\xrightarrow{i}F\to Q\to0.
$$

It follows that $F$ is $\iota$-mixed of weights at most $u$.
