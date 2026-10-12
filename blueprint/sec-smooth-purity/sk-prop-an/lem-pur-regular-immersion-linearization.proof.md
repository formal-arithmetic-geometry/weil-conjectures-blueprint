+++
kind  = "proof"
of    = "lem-pur-regular-immersion-linearization"
+++
The regular–smooth criterion over the perfect field $k$, as in
[lem-sc-smooth-regular], makes $Z$ smooth. Work first at a
closed point $z$, and on the smooth component of $Z$ containing
it, of dimension $m$. Choose local generators $f_1,\ldots,f_c$
of its ideal, possible by [def-pur-regular-immersion].
For this smooth pair the conormal sequence at $z$ is an exact
sequence of vector spaces

$$
0\to (I/I^2)\otimes k(z)\to\Omega_{X/k}\otimes k(z)
\to\Omega_{Z/k}\otimes k(z)\to0.
$$

The first map sends the classes of $f_i$ to $df_i$.
Choose functions $g_1,\ldots,g_m$ on $Z$ whose differentials
form a basis of the last space, and lift them to functions on $X$.
The differentials $df_i,dg_j$ then form a basis of the middle
space. The coordinate map $(f_1,\ldots,f_c,g_1,\ldots,g_m)$
to $\mathbf A^{c+m}_k$ is etale at $z$, by the differential
criterion for the local coordinates in
[sbc-thm-etale-local-normal-form]. Shrink its source so that
it remains etale and the $f_i$ still generate the ideal of $Z$.
Then its inverse image of $x_1=\cdots=x_c=0$ is exactly $Z$,
and its restriction to $Z$ is etale by base change.
These neighborhoods cover all closed points. Their union contains
every point: its closed complement, if nonempty, would contain a
closed point since the schemes are of finite type over a field.
This gives the claimed neighborhoods at arbitrary points as well.
