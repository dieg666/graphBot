// Generated from Enquestes.g by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link EnquestesParser}.
 */
public interface EnquestesListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link EnquestesParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(EnquestesParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link EnquestesParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(EnquestesParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link EnquestesParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(EnquestesParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link EnquestesParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(EnquestesParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link EnquestesParser#assigs}.
	 * @param ctx the parse tree
	 */
	void enterAssigs(EnquestesParser.AssigsContext ctx);
	/**
	 * Exit a parse tree produced by {@link EnquestesParser#assigs}.
	 * @param ctx the parse tree
	 */
	void exitAssigs(EnquestesParser.AssigsContext ctx);
	/**
	 * Enter a parse tree produced by {@link EnquestesParser#question}.
	 * @param ctx the parse tree
	 */
	void enterQuestion(EnquestesParser.QuestionContext ctx);
	/**
	 * Exit a parse tree produced by {@link EnquestesParser#question}.
	 * @param ctx the parse tree
	 */
	void exitQuestion(EnquestesParser.QuestionContext ctx);
	/**
	 * Enter a parse tree produced by {@link EnquestesParser#link}.
	 * @param ctx the parse tree
	 */
	void enterLink(EnquestesParser.LinkContext ctx);
	/**
	 * Exit a parse tree produced by {@link EnquestesParser#link}.
	 * @param ctx the parse tree
	 */
	void exitLink(EnquestesParser.LinkContext ctx);
}