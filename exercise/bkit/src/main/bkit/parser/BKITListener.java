// Generated from BKIT.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(BKITParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(BKITParser.ProgContext ctx);
}